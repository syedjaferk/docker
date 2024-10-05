# Use an official Node.js runtime as a parent image
FROM node:14-slim

# Install curl
RUN apt-get update && apt-get install -y curl procps

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY package*.json ./
COPY app.js ./

# Install any needed packages
RUN npm install

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Run the application
CMD [ "node", "app.js" ]

# Add a HEALTHCHECK instruction
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl --fail http://localhost:3000/health || exit 1
