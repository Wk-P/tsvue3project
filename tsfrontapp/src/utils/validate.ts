export function getCSRFToken(): Promise<string | null> {
    return fetch("/backend/api/csrftoken/")
    .then(response => {
        if (!response.ok) {
            throw new Error("无法获取令牌");
        } else {
            return response.json();
        }
    }).then(data => {
        return data['csrf-token'] || null;
    }).catch( error => {
        console.error("获取 CSRF 令牌失败 :", error.message);
        return null;
    });
}