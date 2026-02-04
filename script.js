document.addEventListener('DOMContentLoaded', () => {
    const scrollTopBtn = document.getElementById('scrollTopBtn');

    // Show/Hide Scroll Top Button
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            scrollTopBtn.classList.add('visible');
        } else {
            scrollTopBtn.classList.remove('visible');
        }
    });

    // Smooth Scroll to Top
    scrollTopBtn.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Highlight active navbar link based on current page
    const currentPath = window.location.pathname.split('/').pop();
    const navLinks = document.querySelectorAll('.nav-links a');

    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });

    // Hamburger Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinksContainer = document.querySelector('.nav-links');

    if (hamburger) {
        hamburger.addEventListener('click', () => {
            navLinksContainer.classList.toggle('active');

            // Optional: Toggle icon between bars and times
            const icon = hamburger.querySelector('i');
            if (navLinksContainer.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });

        // Close menu when clicking a link
        navLinksContainer.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinksContainer.classList.remove('active');
                const icon = hamburger.querySelector('i');
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            });
        });
    }
});

    // Article Functions
    
    // TOC Toggle
    const tocTitle = document.querySelector('.toc-title');
    const tocList = document.querySelector('.toc-list');
    if (tocTitle && tocList) {
        tocTitle.addEventListener('click', () => {
            tocList.classList.toggle('active');
            const icon = tocTitle.querySelector('i');
            if (icon) {
                icon.classList.toggle('fa-chevron-down');
                icon.classList.toggle('fa-chevron-up');
            }
        });
    }

    // Auto Generate TOC if empty
    if (document.querySelector('.article-body')) {
        const headings = document.querySelectorAll('.article-body h2, .article-body h3');
        if (headings.length > 0 && tocList) {
            headings.forEach((heading, index) => {
                const id = 'heading-' + index;
                heading.setAttribute('id', id);
                const li = document.createElement('li');
                const a = document.createElement('a');
                a.href = '#' + id;
                a.textContent = heading.textContent;
                a.style.marginLeft = heading.tagName === 'H3' ? '20px' : '0px';
                li.appendChild(a);
                tocList.appendChild(li);
            });
            // Open by default if we found headings
            tocList.classList.add('active');
        }
    }

    // FAQ Accordion
    const faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(q => {
        q.addEventListener('click', () => {
            const answer = q.nextElementSibling;
            answer.classList.toggle('active');
            const icon = q.querySelector('i');
            if(icon) {
                 icon.classList.toggle('fa-plus');
                 icon.classList.toggle('fa-minus');
            }
        });
    });

