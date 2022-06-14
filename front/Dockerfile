FROM node:16

# Create app directory
WORKDIR /usr/src/app

MKDIR /user/src/app/front
CD /user/src/app/front

# Install app dependencies

COPY front/package*.json ./

RUN npm install

# RUN npm ci --only=production

# Bundle app source
COPY . .

EXPOSE 8080
CMD [ "npm", "serve" ]