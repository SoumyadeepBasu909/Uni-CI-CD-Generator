document.getElementById("pipelineForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const requestData = {
        ci_cd_tool: document.getElementById("ci_cd_tool").value,
        project_type: document.getElementById("project_type").value,
        github_url: document.getElementById("github_url").value,
        build_tool: document.getElementById("build_tool").value,
        deployment: document.getElementById("deployment").value,
        build_command: document.getElementById("build_command").value,
        test_command: document.getElementById("test_command").value,
        artifact: document.getElementById("artifact").value,
        docker_image: document.getElementById("docker_image").value || null
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/generate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(requestData)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const result = await response.text();  
        document.getElementById("output").textContent = result;
    } catch (error) {
        console.error("Error fetching pipeline:", error);
        document.getElementById("output").textContent = "Failed to generate pipeline.";
    }
});
