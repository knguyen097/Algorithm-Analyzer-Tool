
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.widgets import Button
import matplot  # Import execution_times from matplot.py
import random

# Sorting algorithm labels
sortType = ['Bubble Sort', 'Merge Sort', 'Quick Sort', 'LSD Radix Sort', 'MSD Radix Sort']

# Ensure correct data mapping
final_values = np.array(matplot.execution_times)
growth_rate = final_values / 50  # Smooth animation growth over 50 frames

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 5))
plt.subplots_adjust(bottom=0.2)  # Adjust space for buttons

# Initialize bar chart with zero values
values = np.zeros_like(final_values, dtype=float)

num_bars = len(sortType)
bars = ax.barh(sortType, values, color= ['#'+''.join([random.choice('0123456789ABCDEF') 
                                        for j in range(6)]) 
                                        for i in range(num_bars)])

# Set axis labels and limits
ax.set_xlim(0, max(final_values) * 1.2)
ax.set_xlabel('Execution Time')
ax.set_ylabel('Sorting Algorithms')
ax.set_title('Execution Time Comparison for Sorting Algorithms')

# Animation state variables
frame_number = 0
animation_running = True  # Track play/pause state

# Update function for animation
def update(frame):
    global values, frame_number
    if frame_number < 50:
        values += growth_rate  # Increment bar width
        frame_number += 1
        for bar, new_value in zip(bars, values):
            bar.set_width(new_value)
    else:
        ani.event_source.stop()  # Stop animation once it reaches final values

# Play/Pause button function
def toggle_animation(event):
    global animation_running
    if animation_running:
        ani.event_source.stop()
    else:
        ani.event_source.start()
    animation_running = not animation_running  # Toggle state

# Reset button function
def reset_animation(event):
    global values, frame_number, animation_running
    values[:] = 0.0  # Reset values
    frame_number = 0  # Reset frame count
    for bar in bars:
        bar.set_width(0)
    ax.set_xlim(0, max(final_values) * 1.2)  # Reset axis
    plt.draw()  # Redraw the plot
    if not animation_running:
        ani.event_source.start()  # Restart animation if paused

# Create animation
ani = animation.FuncAnimation(fig, update, frames=120, interval=10, repeat=False)

# Play/Pause button
ax_play = plt.axes([0.7, 0.05, 0.1, 0.075])
btn_play = Button(ax_play, 'Play/Pause')
btn_play.on_clicked(toggle_animation)

# Reset button
ax_reset = plt.axes([0.81, 0.05, 0.1, 0.075])
btn_reset = Button(ax_reset, 'Reset')
btn_reset.on_clicked(reset_animation)

# Show plot
plt.show()
