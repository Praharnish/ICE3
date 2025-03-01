def process_temperatures(temperatures):
    # Check if the input list is empty
    if not temperatures:
        return "No input provided."

    # Initialize variables to track minimum, maximum, total temperature, and count of valid entries
    min_temp = float('inf')  # Start with the highest possible value
    max_temp = float('-inf') # Start with the lowest possible value
    total_temp = 0           # To accumulate the total temperature
    valid_count = 0          # To count how many valid temperatures we have

    # Iterate through each temperature in the input list
    for temp in temperatures:
        try:
            # Attempt to convert the temperature to a float
            temp = float(temp)

            # Check if the temperature is within the acceptable range
            if temp < -50 or temp > 150:
                return "Out-of-bound value detected."

            # Update the minimum and maximum temperatures if necessary
            if temp < min_temp:
                min_temp = temp
            if temp > max_temp:
                max_temp = temp

            # Add the valid temperature to the total and increment the count
            total_temp += temp
            valid_count += 1

        except ValueError:
            # Handle the case where the input cannot be converted to a float
            return "Invalid input detected."

    # After processing all temperatures, check if we have any valid entries
    if valid_count == 0:
        return "No valid input provided."

    # Calculate the average temperature
    avg_temp = total_temp / valid_count

    # Return the results in a formatted string
    return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp:.2f}°C"