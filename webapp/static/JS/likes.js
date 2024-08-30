document.addEventListener('DOMContentLoaded', function () {
    const likeButtons = document.querySelectorAll('.like-button');
    const unlikeButtons = document.querySelectorAll('.unlike-button');

    likeButtons.forEach(button => {
        button.addEventListener('click', function () {
            const postId = this.dataset.postId;
            likePost(postId);
        });
    });

    unlikeButtons.forEach(button => {
        button.addEventListener('click', function () {
            const postId = this.dataset.postId;
            unlikePost(postId);
        });
    });
});

function likePost(postId) {
    fetch(`/api/v1/posts/${postId}/like/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        credentials: 'same-origin'
    })
    .then(response => {
        if (response.ok) {
            alert('Post liked!');
        } else {
            alert('Failed to like post.');
        }
    })
    .catch(error => console.error('Error:', error));
}

function unlikePost(postId) {
    fetch(`/api/v1/posts/${postId}/unlike/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        credentials: 'same-origin'
    })
    .then(response => {
        if (response.ok) {
            alert('Post unliked!');
        } else {
            alert('Failed to unlike post.');
        }
    })
    .catch(error => console.error('Error:', error));
}


function getCSRFToken() {
    let cookieValue = null;
    const name = 'csrftoken';
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
