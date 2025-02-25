import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.widgets import Button

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
final_values = np.array([10, 20, 15, 25, 30], dtype=float)  # Ensure float dtype
growth_rate = final_values / 50  # Slow growth over 50 frames

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 5))
plt.subplots_adjust(bottom=0.2)  # Adjust space for buttons

# Create bars with initial zero values (as float)
values = np.zeros_like(final_values, dtype=float)  # Ensure it's float
bars = ax.barh(categories, values, color='skyblue')

# Set axis limits
ax.set_xlim(0, max(final_values) * 1.2)
ax.set_xlabel('Values')
ax.set_ylabel('Categories')
ax.set_title('Slow Growth in Horizontal Bar Chart')

# Animation variables
frame_number = 0

# Update function for animation
def update(frame):
    global values, frame_number
    if frame_number < 50:  # 50 frames for slow growth
        values += growth_rate  # Increment values slowly
        frame_number += 1
        for bar, new_value in zip(bars, values):
            bar.set_width(new_value)  # Update bar width
        ax.set_xlim(0, max(final_values) * 1.2)  # Adjust x-axis dynamically
    else:
        # Reset values and frame number after each loop
        values[:] = 0.0  # Reset values to 0 (ensure float)
        frame_number = 0  # Reset frame counter
        # This will allow continuous replay without manually starting/stopping the animation
        ani.event_source.stop()  # Stop the animation after completing
        ani.event_source.start()  # Restart the animation

# Play/Pause button function
def toggle_animation(event):
    if ani.event_source.running:
        ani.event_source.stop()
    else:
        ani.event_source.start()

# Reset button function
def reset_animation(event):
    global values, frame_number
    values[:] = 0.0  # Reset values to 0
    frame_number = 0  # Reset frame counter
    for bar, new_value in zip(bars, values):
        bar.set_width(new_value)  # Update bars
    plt.draw()  # Redraw the plot

# Create animation with looping enabled
ani = animation.FuncAnimation(fig, update, frames=50, interval=200, repeat=True)

# Add Play/Pause button
ax_play = plt.axes([0.7, 0.05, 0.1, 0.075])
btn_play = Button(ax_play, 'Play/Pause')
btn_play.on_clicked(toggle_animation)

# Add Reset button
ax_reset = plt.axes([0.81, 0.05, 0.1, 0.075])
btn_reset = Button(ax_reset, 'Reset')
btn_reset.on_clicked(reset_animation)

# Show plot
plt.show()
