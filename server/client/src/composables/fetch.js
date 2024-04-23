import { useAccessToken } from "./auth";

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