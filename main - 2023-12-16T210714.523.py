import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.backend_bases import PickEvent

class InteractiveBoxDrawer:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.box = Rectangle((0.5, 0.5), 0.2, 0.2, edgecolor='r', facecolor='none')
        self.ax.add_patch(self.box)

        self.fig.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)

    def on_mouse_move(self, event):
        if isinstance(event, PickEvent):
            x, y = event.mouseevent.xdata, event.mouseevent.ydata
            self.update_box_position(x, y)

    def update_box_position(self, x, y):
        box_width = 0.2
        box_height = 0.2
        self.box.set_x(x - box_width / 2)
        self.box.set_y(y - box_height / 2)
        self.fig.canvas.draw()

    def show_plot(self):
        plt.show()

if __name__ == "__main__":
    drawer = InteractiveBoxDrawer()
    drawer.show_plot()
