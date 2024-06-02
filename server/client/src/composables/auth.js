export function useCheckAuth() {
    return localStorage.getItem('token')
}

export function useAccessToken() {
    let access_token = localStorage.getItem('token');
    access_token = JSON.parse(access_token)?.access_token
    return access_token
}
function jwtDecode(t) {
  let token = {};
  token.raw = t;
  token.header = JSON.parse(window.atob(t.split('.')[0]));
  token.payload = JSON.parse(window.atob(t.split('.')[1]));
    console.log(token);
  return (token)
}

export function is_student() {
    return jwtDecode(useAccessToken()).payload.role == 'student';
}
