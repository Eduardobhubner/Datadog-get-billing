# Datadog Consumption Syout Script

## Requirements

- API_KEY
- DD_KEY
- DATE_KEY (optional, default: date_now)
- URL (optional, default: US1)

## Output

- Sub organization
- License
- Consumption

## Building Image
`docker build -t (NAME-BUILD):TAG .`

## Running Image
`docker run -e API_KEY=your_api_key -e DD_KEY=your_dd_key  -e DATA_KEY=data(YYYY-MM) -e URL_KEY=url image_name`

## Push Image

```
    docker build -t dc-billing:latest .  
    docker tag dc-billing eduardobhubner/dc-billing
    docker login
    docker push eduardobhubner/dc-billing (could also be done through the interactive button on the desktopHub which also works)

```


