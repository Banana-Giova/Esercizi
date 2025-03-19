let fetchAllPosts = () => {
    return fetch('https://jsonplaceholder.typicode.com/posts')
        .then(response => {
            if (!response.ok) {
                throw new Error('Errore nella richiesta')
            }
            return response.json();
        })
}

let fetchOnePost = (postId) => {
    return fetch(`https://jsonplaceholder.typicode.com/posts/${postId}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Errore nella richiesta')
            }
            return response.json();
        })
}

let fetchAllComments = (postId) => {
    return fetch(`https://jsonplaceholder.typicode.com/posts/${postId}/comments`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Errore nella richiesta')
            }
            return response.json();
        })
}

let constructPost = (post) => {
    // add anchor
    return `
    <div class="exercise-container">
        <div class="post-header">
            <h4 class="user-id">User ID: ${post.userId}</h4>
            <h3 class="post-id">${post.id}</h3>
            <h2 class="post-title">${post.title}</h2>
        </div>
        <div class="post-body">
            <p>${post.body}</p>
        </div>
    </div>


    `;
}

let mainPosts = (resultId) => {
    let result_html = "";
    fetchAllPosts()
        .then(data => {
            data.forEach(post => {
                result_html += constructPost(post);
            });
        
            document.getElementById(resultId).innerHTML = result_html;
        })
        .catch(error => {
            console.error("Errore:", error);
        });
}