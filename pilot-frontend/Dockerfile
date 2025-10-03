# Build stage
FROM node:20-alpine AS builder

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY . .

# Build the application
RUN npm run build

# Production stage
FROM node:20-alpine

WORKDIR /app

# Copy package files first
COPY --from=builder /app/package*.json ./

# Install only production dependencies (needed for SvelteKit runtime)
RUN npm ci --omit=dev

# Copy built assets from builder stage
COPY --from=builder /app/build ./build

EXPOSE 3000

ENV NODE_ENV=production
ENV HOST=0.0.0.0
ENV PORT=3000

CMD ["node", "build/index.js"]
