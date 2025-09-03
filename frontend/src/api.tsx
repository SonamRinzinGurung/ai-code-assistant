export async function getExplanation(code: string) {
    const response = await fetch("http://127.0.0.1:8000/api/explain", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code })
    })
    return response.json()
}