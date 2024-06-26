document.addEventListener('DOMContentLoaded', function() {
    const table = document.querySelector('#partners-table tbody');
    const rows = table.querySelectorAll('tr');
    const rowsPerPage = 10;
    const pagination = document.querySelector('#pagination');
    let currentPage = 1;

    function paginateTable(page) {
        const start = (page - 1) * rowsPerPage;
        const end = start + rowsPerPage;

        rows.forEach((row, index) => {
            if (index >= start && index < end) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    }

    function createPaginationControls() {
        const pageCount = Math.ceil(rows.length / rowsPerPage);
        pagination.innerHTML = '';

        // Ensure that only a limited number of page links are displayed
        const maxPagesToShow = 10; // Adjust as needed
        let startPage = Math.max(currentPage - Math.floor(maxPagesToShow / 2), 1);
        let endPage = startPage + maxPagesToShow - 1;
        
        if (endPage > pageCount) {
            endPage = pageCount;
            startPage = Math.max(endPage - maxPagesToShow + 1, 1);
        }

        // Previous page button
        const prevLi = document.createElement('li');
        prevLi.classList.add('page-item');
        if (currentPage === 1) {
            prevLi.classList.add('disabled');
        }
        const prevLink = document.createElement('a');
        prevLink.classList.add('page-link');
        prevLink.href = '#';
        prevLink.innerHTML = 'Previous';
        prevLi.appendChild(prevLink);
        pagination.appendChild(prevLi);

        // Numbered page links
        for (let i = startPage; i <= endPage; i++) {
            const li = document.createElement('li');
            li.classList.add('page-item');
            if (i === currentPage) {
                li.classList.add('active');
            }
            const link = document.createElement('a');
            link.classList.add('page-link');
            link.href = '#';
            link.innerHTML = i;
            li.appendChild(link);
            pagination.appendChild(li);
        }

        // Next page button
        const nextLi = document.createElement('li');
        nextLi.classList.add('page-item');
        if (currentPage === pageCount) {
            nextLi.classList.add('disabled');
        }
        const nextLink = document.createElement('a');
        nextLink.classList.add('page-link');
        nextLink.href = '#';
        nextLink.innerHTML = 'Next';
        nextLi.appendChild(nextLink);
        pagination.appendChild(nextLi);

        // Event listeners for pagination controls
        const pageLinks = pagination.querySelectorAll('.page-link');
        pageLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                if (this.innerHTML === 'Previous') {
                    handlePagination(currentPage - 1);
                } else if (this.innerHTML === 'Next') {
                    handlePagination(currentPage + 1);
                } else {
                    handlePagination(parseInt(this.innerHTML));
                }
            });
        });

        // Initialize pagination
        handlePagination(1);
    }

    function handlePagination(page) {
        if (page < 1) {
            page = 1;
        } else if (page > Math.ceil(rows.length / rowsPerPage)) {
            page = Math.ceil(rows.length / rowsPerPage);
        }
        currentPage = page;
        paginateTable(currentPage);

        // Update active class
        const pageItems = pagination.querySelectorAll('.page-item');
        pageItems.forEach(item => item.classList.remove('active', 'disabled'));
        const activePageItem = [...pageItems].find(item => item.textContent === String(currentPage));
        if (activePageItem) {
            activePageItem.classList.add('active');
        }
        if (currentPage === 1) {
            pageItems[0].classList.add('disabled');
        }
        if (currentPage === Math.ceil(rows.length / rowsPerPage)) {
            pageItems[pageItems.length - 1].classList.add('disabled');
        }
    }

    createPaginationControls();
});
