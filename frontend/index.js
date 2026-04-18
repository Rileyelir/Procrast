window.addEventListener("pywebviewready", function() {
    console.log("index.js - pywebview ready");

    const newProj = document.querySelector("#newproject")
    newProj.addEventListener("click", async function() {
        pywebview.api.hello();
    })
})