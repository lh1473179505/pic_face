pic_face
========

pic_face image and video face toolkit.


Installation
------------

```
conda create --name pic_face python=3.12 pip=25.0
conda activate pic_face
python install.py default
```

On Windows with DirectML:

```
python install.py directml
```


Usage
-----

```
python pic_face.py run --open-browser
```

Headless:

```
python pic_face.py headless-run -s source.jpg -t target.jpg -o output.jpg
```

```
python pic_face.py [commands] [options]

commands:
    run                                           run the program
    headless-run                                  run the program in headless mode
    batch-run                                     run the program in batch mode
    force-download                                force automate downloads and exit
    benchmark                                     benchmark the program
    job-list                                      list jobs by status
    job-create                                    create a drafted job
    job-submit                                    submit a drafted job to become a queued job
    job-submit-all                                submit all drafted jobs to become a queued jobs
    job-delete                                    delete a drafted, queued, failed or completed job
    job-delete-all                                delete all drafted, queued, failed and completed jobs
    job-add-step                                  add a step to a drafted job
    job-remix-step                                remix a previous step from a drafted job
    job-insert-step                               insert a step to a drafted job
    job-remove-step                               remove a step from a drafted job
    job-run                                       run a queued job
    job-run-all                                   run all queued jobs
    job-retry                                     retry a failed job
    job-retry-all                                 retry all failed jobs
```
