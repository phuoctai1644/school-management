document.addEventListener('DOMContentLoaded', () => {
    const submitBtn = document.querySelector('#submit-button')
    submitBtn.addEventListener('click', () => {
        const form = document.querySelector('#edit-form')
        form.submit()
    })
})
