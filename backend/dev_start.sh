
docker run -it --rm --name dashboard_backend_1 \
    --publish 8081:8081 \
    --volume $PWD/:/app \
    --volume $PWD/../log/:/log \
    --volume $PWD/../archive/:/archive \
    --env-file $PWD/../.env \
    dashboard_backend
#    --network survey_progress_survey \
#    survey_progress_backend

