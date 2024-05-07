/** @type {import('next').NextConfig} */
const nextConfig = {
    async headers() {
        return [
            {
                // matching all API routes
                source: "/api/:path*",
                headers: [
                    { key: "Access-Control-Allow-Origin", value: "http://127.0.0.1:5000/" }, // replace this your actual origin

                ]
            }
        ]
    }
}

export default nextConfig;
