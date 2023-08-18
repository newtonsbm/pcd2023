FROM node:14-alpine3.12
RUN mkdir /code
COPY . /code
WORKDIR  /code/barao_pcd
RUN yarn install 
EXPOSE 8000
CMD [ "yarn", "dev", "-p", "8000" ]
