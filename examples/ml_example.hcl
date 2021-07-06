# File: examples/ml_example.hcl

flow "machine_learning_example" {

  import {
    tasks = {
      extract = "examples.sklearn_refactored_script:ExtractTrainingSet"
      train_model = "examples.sklearn_refactored_script:TrainModel"
    }
  }

  task "extract" "setup" {
  }

  task "train_model" "model1" {
    model = "ols"
    x = task.extract.setup.x
    y = task.extract.setup.y
  }

  task "train_model" "model2" {
    model = "gbm"
    x = task.extract.setup.x
    y = task.extract.setup.y
  }

  task "file_write" "output" {
    filename = "/dev/stdout"
    content = tojson({
      scores = {
        ols = task.train_model.model1.score
        gbm = task.train_model.model2.score
      }
    }, { indent = 2 }...)
  }

}
