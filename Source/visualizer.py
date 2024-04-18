import pygame
import random
import time

pygame.init()

# Constants for easy modification
BACKGROUND_COLOR = (30, 30, 30)
BAR_COLOR = (217, 212, 195)
HIGHLIGHT_COLOR = (212, 169, 121)
FONT = pygame.font.SysFont('Consolas', 20)
BUTTON_FONT = pygame.font.SysFont('Consolas', 18)
COLORS = [(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)) for _ in range(100)]

class SortingVisualizer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Advanced Sorting Algorithm Visualizer")
        self.array = []
        self.generate_new_array(50, 10, 100)
        self.algorithms = {'Bubble Sort': self.bubble_sort, 'Insertion Sort': self.insertion_sort, 'Selection Sort': self.selection_sort}
        self.current_algorithm = 'Bubble Sort'
        self.ascending = True
        self.sorting = False
        self.start_time = 0
        self.elapsed_time = 0

    def generate_new_array(self, size, min_val, max_val):
        self.array = [(random.randint(min_val, max_val), random.choice(COLORS)) for _ in range(size)]
        self.bar_width = (self.width - 100) / len(self.array)
        self.bar_height = (self.height - 150) / max([num for num, color in self.array])

    def draw(self):
        self.window.fill(BACKGROUND_COLOR)
        self.draw_bars()
        self.draw_ui()
        pygame.display.update()

    def draw_bars(self):
        for i, (value, color) in enumerate(self.array):
            x = 50 + i * self.bar_width
            y = self.height - 100 - value * self.bar_height
            pygame.draw.rect(self.window, color, (x, y, max(1, self.bar_width - 2), value * self.bar_height))

    def draw_ui(self):
        status_text = f"Algorithm: {self.current_algorithm} - {'Ascending' if self.ascending else 'Descending'}"
        timer_text = f"Time Elapsed: {self.elapsed_time:.2f}s"
        status = FONT.render(status_text, True, BAR_COLOR)
        timer = FONT.render(timer_text, True, BAR_COLOR)
        self.window.blit(status, (10, 10))
        self.window.blit(timer, (10, 40))
        for i, algo in enumerate(self.algorithms):
            button_color = HIGHLIGHT_COLOR if algo == self.current_algorithm else BAR_COLOR
            button = BUTTON_FONT.render(f"{algo}", True, button_color)
            self.window.blit(button, (10, 70 + i * 30))

    def update_time(self):
        if self.sorting:
            self.elapsed_time = time.time() - self.start_time

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n-i-1):
                if (self.array[j][0] > self.array[j+1][0] and self.ascending) or (self.array[j][0] < self.array[j+1][0] and not self.ascending):
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    self.draw()
                    self.update_time()
                    yield True
        self.sorting = False

    def insertion_sort(self):
        n = len(self.array)
        for i in range(1, n):
            key = self.array[i]
            j = i - 1
            while j >= 0 and ((key[0] < self.array[j][0] and self.ascending) or (key[0] > self.array[j][0] and not self.ascending)):
                self.array[j + 1] = self.array[j]
                j -= 1
                self.array[j + 1] = key
                self.draw()
                self.update_time()
                yield True
        self.sorting = False

    def selection_sort(self):
        n = len(self.array)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if (self.array[j][0] < self.array[min_idx][0] and self.ascending) or (self.array[j][0] > self.array[min_idx][0] and not self.ascending):
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.draw()
            self.update_time()
            yield True
        self.sorting = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.generate_new_array(50, 10, 100)
                    self.sorting = False
                elif event.key == pygame.K_SPACE and not self.sorting:
                    self.sorting = True
                    self.start_time = time.time()
                    self.sort_algorithm = self.algorithms[self.current_algorithm]()
                elif event.key in (pygame.K_a, pygame.K_d):
                    self.ascending = (event.key == pygame.K_a)
                elif event.key in (pygame.K_b, pygame.K_i, pygame.K_s):
                    self.current_algorithm = {'b': 'Bubble Sort', 'i': 'Insertion Sort', 's': 'Selection Sort'}[chr(event.key)]
                    self.sorting = False
        return True

    def run(self):
        clock = pygame.time.Clock()
        while self.handle_events():
            if self.sorting:
                try:
                    next(self.sort_algorithm)
                except StopIteration:
                    self.sorting = False
                    self.elapsed_time = time.time() - self.start_time
            self.draw()
            clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    visualizer = SortingVisualizer(800, 600)
    visualizer.run()
