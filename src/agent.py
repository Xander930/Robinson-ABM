import numpy as np


class AgentAnt:
    def __init__(self, agent_id, x_start, y_start):
        self.id = agent_id
        self.threshold_alpha = np.random.normal(loc=5.0, scale=1.0)

        self.x = x_start
        self.y = y_start
        self.state = (
            "Searching"  # Current state, either 'Searching', 'Committed', or 'Home'
        )
        self.committed_nest_qual = None

    def move(self, env_width, env_height):
        dx = np.random.choice([-1, 0, 1])
        dy = np.random.choice([-1, 0, 1])

        x_new = max(0, min(env_width - 1, self.x + dx))
        y_new = max(0, min(env_height - 1, self.y + dy))

        self.x = x_new
        self.y = y_new

    def assess_and_choose(self, patch):
        if not patch.is_nest:
            return

        assess_error = np.random.normal(loc=0, scale=1.0)
        sample_quality = patch.quality + assess_error

        if sample_quality > self.threshold_alpha:
            self.state = "Committed"
            self.committed_nest_qual = patch.quality