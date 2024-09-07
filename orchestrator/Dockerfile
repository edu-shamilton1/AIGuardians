# Use a Node.js base image with a specific version (e.g., 18-alpine)
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json   
# (if present) to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest   
# of your application code
COPY src/ ./src/

# Expose port 3001
EXPOSE 3001

# Define the command to run when the container starts
CMD ["node", "src/index.js"]
