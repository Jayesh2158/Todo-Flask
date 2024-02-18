Build Image
docker build -t {{New-image-name}} .

Run Container
docker run -dp 3000:3000 {{existing-image-name}}


This is a web application built with Flask. It is a learnig project for creating REST API in Flask. And it also contain experience level integration before deployment like logging, docker compose and app structure etc.