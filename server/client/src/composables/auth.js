export function useCheckAuth() {
    return localStorage.getItem('token')
}

export function useAccessToken() {
    let access_token = localStorage.getItem('token');
    access_token = JSON.parse(access_token)?.access_token
    return access_token
}