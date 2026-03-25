document.addEventListener('DOMContentLoaded', function () {
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileMenu = document.getElementById('mobileMenu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function () {
            mobileMenu.classList.toggle('open');
        });
    }

    document.querySelectorAll('.product-card').forEach(function (card) {
        card.addEventListener('mouseenter', function () {
            this.style.transform = 'translateY(-4px)';
            this.style.transition = 'transform 0.25s ease';
        });
        card.addEventListener('mouseleave', function () {
            this.style.transform = '';
        });
    });

    document.querySelectorAll('.cat-card').forEach(function (card) {
        card.addEventListener('click', function (e) {
            this.style.transform = 'scale(0.96)';
            setTimeout(() => { this.style.transform = ''; }, 120);
        });
    });

    const addToCartForm = document.querySelector('.add-to-cart-form');
    if (addToCartForm) {
        addToCartForm.addEventListener('submit', function (e) {
            const sizeSelected = this.querySelector('input[name="size"]:checked');
            if (!sizeSelected) {
                e.preventDefault();
                const sizeGrid = document.getElementById('sizeGrid');
                if (sizeGrid) {
                    sizeGrid.style.outline = '2px solid red';
                    sizeGrid.style.outlineOffset = '4px';
                    sizeGrid.style.borderRadius = '8px';
                    setTimeout(() => {
                        sizeGrid.style.outline = '';
                        sizeGrid.style.outlineOffset = '';
                    }, 2000);
                    sizeGrid.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
                alert('Please select a size first.');
            }
        });
    }

    document.querySelectorAll('img').forEach(function (img) {
        img.addEventListener('error', function () {
            this.src = 'https://via.placeholder.com/400x400/f5f5f5/111111?text=Nike';
            this.onerror = null;
        });
    });
});
