FROM node AS build

WORKDIR /app


COPY package.json package-lock.json ./
RUN npm ci

COPY . .

RUN npm run build

FROM node 

WORKDIR /app

COPY public public
COPY package.json package-lock.json ./
RUN npm ci --omit-dev
COPY --from=build /app/.next .next

CMD ["npm", "run", "start"]
