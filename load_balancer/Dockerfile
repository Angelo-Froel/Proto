FROM nginx:1.22.1

# Install Nginx module for Perl support
RUN apt-get update && \
    apt-get install -y libnginx-mod-http-perl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy custom Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
