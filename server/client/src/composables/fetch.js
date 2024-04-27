import { useAccessToken } from "./auth";
import { useRouter } from "vue-router";
const router = useRouter();

export async function useFetch(path, params, method, data) {
    const url = new URL(path, location.origin);
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))

    var options = {
        headers: {
            'Content-Type': 'application/json',
            "Authorization": `Bearer ${useAccessToken()}`
        },
    }
    if (method === 'POST') options['method'] = 'POST';
    if (data) options['body'] = JSON.stringify(data);

    let response = await fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json',
            "Authorization": `Bearer ${useAccessToken()}`
        },
        body: JSON.stringify(data)
    })
    response = await response.json()
    return response
}

export async function useAttendance() {
  let response = await fetch('/api_1/get_attendance', {
    headers: {
      'Authorization' : `Bearer ${useAccessToken()}`
    }
  })
  response = await response.json()
  console.log(response)
  return response
}

export async function useStudents() {
  let response = await fetch('/api_1/get_students', {
    headers: {
      'Authorization' : `Bearer ${useAccessToken()}`
    }
  })
  response = await response.json()
  console.log(response)
  return response
}
