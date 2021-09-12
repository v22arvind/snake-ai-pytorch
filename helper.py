import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(scores, mean_scores, rnd_moves, predicted_moves):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores, label = 'Score')
    plt.plot(mean_scores, label = 'Mean Score')
    plt.plot(rnd_moves, label = 'Rnd Moves')
    #plt.plot(predicted_moves)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.legend()
    plt.show(block=False)
    plt.pause(.1)
