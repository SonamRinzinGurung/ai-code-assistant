import { useState } from "react"
import { getExplanation } from "../api"


function CodeEditor() {
    const [code, setCode] = useState("")
    const [output, setOutput] = useState("")

    const handleExplain = async () => {
        const result = await getExplanation(code)
        setOutput(result.explanation)
    }
    return <div className="flex flex-col gap-4">
        <textarea
            value={code}
            onChange={(e) => setCode(e.target.value)}
            className="w-full h-40 border rounded p-2 font-mono"
        />
        <button
            onClick={handleExplain}
            className="bg-blue-500 text-white px-4 py-2 rounded"
        >
            Explain Code
        </button>
        <pre className="bg-gray-100 p-4 rounded whitespace-pre-wrap">{output}</pre>
    </div>
}

export default CodeEditor