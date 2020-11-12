# pr_curve
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/pr_curve.py#L9-L105)

`def pr_curve(y_true=None, y_probas=None, labels=None, classes_to_plot=None)`



Computes the tradeoff between precision and recall for different thresholds.
A high area under the curve represents both high recall and high precision,
where high precision relates to a low false positive rate, and high recall
relates to a low false negative rate. High scores for both show that the
classifier is returning accurate results (high precision), as well as
returning a majority of all positive results (high recall).
PR curve is useful when the classes are very imbalanced.








**Reutrns**

Nothing. To see plots, go to your W&B run page then expand the 'media' tab
under 'auto visualizations'.



