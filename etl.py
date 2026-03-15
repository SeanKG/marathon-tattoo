import pandas as pd
import matplotlib.pyplot as plt

def main():
    # 1. Load the raw data
    print("Loading raw heart rate data...")
    df = pd.read_csv('heart_rate_2017-10-08.csv')

    # Convert timestamp to datetime objects (handling UTC)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # 2. Define start and end times for the marathon
    # Race started at 7:30 AM local, which is 10:30 AM UTC
    # Finished in roughly 5 hours, 11 minutes
    start_time = pd.Timestamp('2017-10-08 10:30:00', tz='UTC')
    end_time = start_time + pd.Timedelta(hours=5, minutes=11)

    # 3. Filter and sort the data
    print("Filtering data for marathon duration...")
    race_data = df[(df['timestamp'] >= start_time) & (df['timestamp'] <= end_time)].copy()
    race_data = race_data.sort_values('timestamp')

    print(f"Extracted {len(race_data)} data points for the race.")

    # 4. Save the filtered dataset
    csv_filename = 'marathon_heart_rate_data.csv'
    race_data.to_csv(csv_filename, index=False)
    print(f"Filtered data saved to {csv_filename}")

    # 5. Generate Standard Analytical Plot
    plt.figure(figsize=(12, 6))
    plt.plot(race_data['timestamp'], race_data['beats per minute'], color='black', linewidth=1)
    plt.title('Marathon Heart Rate Profile')
    plt.xlabel('Time (UTC)')
    plt.ylabel('Heart Rate (BPM)')
    plt.grid(False)
    
    standard_plot_filename = 'marathon_heart_rate_graph.png'
    plt.savefig(standard_plot_filename)
    print(f"Standard plot saved to {standard_plot_filename}")

    # 6. Generate Clean Tattoo Design Plot (Horizontal)
    plt.figure(figsize=(10, 4))
    plt.plot(race_data['timestamp'], race_data['beats per minute'], color='black', linewidth=1.5)
    plt.axis('off') # Turn off all axes and labels for a cleaner stencil look
    plt.tight_layout()
    
    clean_plot_filename = 'marathon_heart_rate_tattoo_design.png'
    plt.savefig(clean_plot_filename, bbox_inches='tight', pad_inches=0)
    print(f"Clean tattoo design saved to {clean_plot_filename}")

if __name__ == "__main__":
    main()