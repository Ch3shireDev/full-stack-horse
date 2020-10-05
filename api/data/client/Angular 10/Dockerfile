FROM node:14.2.0-alpine3.11 as build
WORKDIR /app

RUN npm install -g @angular/cli

COPY ./package.json .
RUN npm install
RUN npm ci
COPY . .
RUN ng build --prod

FROM nginx as runtime
COPY --from=build /app/dist/client /usr/share/nginx/html
EXPOSE 80
