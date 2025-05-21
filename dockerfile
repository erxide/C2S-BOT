FROM oven/bun:1.2.2 AS builder

WORKDIR /install

COPY bun.lock package.json ./

RUN bun install --no-progress

FROM oven/bun:1.2.2 AS final

WORKDIR /app

COPY --from=builder /install/node_modules ./node_modules
COPY --from=builder /install/package.json ./package.json
COPY --from=builder /install/bun.lock ./bun.lock

COPY ./src ./src

COPY config.json config.json

CMD [ "bun", "run", "start" ]