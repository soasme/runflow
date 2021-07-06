---
sidebar: auto
---

# Use Scikit-Learn and Runflow

If you're not familiar with [Scikit-learn](https://scikit-learn.org/) and [Runflow](https://runflow.org),

* Scikit-learn is a simple and efficient tools for predictive data analysis.
* Runflow is a tool to define and run workflows.

By mix using both, your machine learning code will be organized better.

## Why Runflow is Needed?

If you just simply follow the code snippets shown on scikit-learn documentation,
you will quickly get into some issues.

* With more complexity added, the code doesn't scale well.
* The code is hard to maintain and read.
* You need to deal with where to load and save the data.
* You need to track the change of models and parameters over time.
* Code change in the middle of the script may break the following code. Spend a lot of time troubleshooting.

## How to Improve Your Machine Learning Code?

Let's see how Runflow solve this issue.

Step 1, split your code into minimal chunk of classes and functions so they're easy to be re-used. And more importantly, the error is contained in a scope.

<<< @/examples/sklearn_refactored_script.py

Step 2, define a data flow using Runflow.

<<< @/examples/ml_example.hcl

::: details Click me the view the output
Run:
```hcl
[2021-07-06 23:15:19,999] "task.extract.setup" is started.
[2021-07-06 23:15:20,006] "task.extract.setup" is successful.
[2021-07-06 23:15:20,006] "task.train_model.model2" is started.
[2021-07-06 23:15:20,144] "task.train_model.model2" is successful.
[2021-07-06 23:15:20,144] "task.train_model.model1" is started.
[2021-07-06 23:15:20,151] "task.train_model.model1" is successful.
[2021-07-06 23:15:20,152] "task.file_write.output" is started.
{
  "scores": {
    "ols": 0.7406426641094095,
    "gbm": 0.9761405838418584
  }
}
[2021-07-06 23:15:20,153] "task.file_write.output" is successful.
```
:::

## Conclusion

Writing machine learning code in spaghetti coding style may create problems for you.
Considering the complex dependencies, it's better to define them as a flow of tasks.
Runflow is one of the competitive solutions.
