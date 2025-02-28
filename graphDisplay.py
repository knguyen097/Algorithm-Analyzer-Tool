
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.widgets import Button
import matplot  # Import execution_times from matplot.py
import random


# Setting global variables for display
final_values = None
growth_rate = None
sortType = None
bars = None
ax = None
fig = None
values = None  # Store bar heights
ani = None  # Animation object
frame_number = 0
animation_running = True  # Track play/pause state


def buildDisplay(selectedAlgos, executionTimes):
    global final_values, growth_rate, sortType, bars, ax, fig, values

    # Ensure correct data mapping
    final_values = np.array(executionTimes)
    sortType = selectedAlgos
    growth_rate = np.where(final_values != 0, final_values / 50, 0)

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
    showPlot()

    





# Show plot
def showPlot():
    global ani
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
        global values, frame_number, animation_running, ani
        values[:] = 0.0  
        frame_number = 0  
        for bar in bars:
            bar.set_width(0)
        ax.set_xlim(0, max(final_values) * 1.2 if np.any(final_values) else 1)  # Reset axis
        plt.draw() 
        if ani is not None:
            ani.event_source.stop()
        

        ani = animation.FuncAnimation(fig, update, frames=50, interval=100, repeat=False)
        animation_running = True  

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
    plt.show()
