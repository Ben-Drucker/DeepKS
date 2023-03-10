import scipy, math, inspect, numpy as np
from typing import Union, Callable
from matplotlib import pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = "P052"

def raw_score_to_probability(
    scores: list[Union[float, int]], truths: list[bool], incr=0.2, plot=False, true_cdf=None, print_eqn=False, eqn_passthrough=None
) -> Callable[[Union[int, float, list[Union[float, int]]]], float]:
    assert all(isinstance(x, (int, float)) for x in scores), f"`{inspect.stack()[0][3]}` requires scores to be numeric."
    assert all(isinstance(x, bool) for x in truths), f"`{inspect.stack()[0][3]}` requires truths to be boolean."
    assert sorted(scores) == scores, f"`{inspect.stack()[0][3]}` requires sorted scores as input."
    assert len(scores) == len(truths), f"`{inspect.stack()[0][3]}` requires equal length of scores and truths."
    i = 0
    places = int(np.ceil(-np.log10(incr)))
    l_orig = round(np.floor(min(scores) * 10 ** places) / 10 ** places, places)
    l = l_orig
    r = l + incr
    probs = []
    midpoints = []
    while i < len(scores):
        count = 0
        total = 0
        while i < len(scores) and l <= scores[i] < r:
            if truths[i]:
                count += 1
            total += 1
            i += 1
        if total != 0:
            midpoints.append(mp := (l + r) / 2)  # type: ignore
            probs.append(prob := count / total)  # type: ignore
            # print("Cutoff {:.3f} = Prob {:.4f}".format(mp, prob))
        l += incr
        r += incr
    base_fn = lambda x, c, d: 1 / (1 + math.e ** (-c * (x - d)))
    params, *_ = scipy.optimize.curve_fit(base_fn, midpoints, probs)
    if print_eqn:
        print("Equation --- ")
        print("Let x be the raw score, then the probability of being a true hit is:")
        print("P(x) = 1 / (1 + e^(-{c:.3f} * (x - {d:.3f})))")
    if eqn_passthrough is not None:
        eqn_passthrough['form'] = lambda x, c, d: 1 / (1 + math.e ** (-c * (x - d)))
        eqn_passthrough['params'] = params

    convert_fn = lambda x: base_fn(x, *params)
    if plot:
        plt.plot(midpoints, probs, "go-", label="Actual Data", markersize=1, linewidth=0.5)
        X = np.linspace(l_orig, max(scores), endpoint=True, num=1000)
        plt.plot(X, [convert_fn(x) for x in X], label="Approximated function(raw score) => probability", linewidth=0.5)
        if true_cdf is not None:
            plt.plot(X, [true_cdf(x) / true_cdf(10) for x in X], label="True function(raw score) => probability", linewidth=0.5)
        plt.legend()
        plt.xlabel("Raw score")
        plt.ylabel("Estimated non-decoy fraction given raw score")
        plt.title("Converting raw score into a true estimated probability")
    return convert_fn
