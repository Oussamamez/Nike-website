const PLACEHOLDER = '/static/images/placeholder.svg';

document.addEventListener('DOMContentLoaded', function () {
    // Mobile menu toggle
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function () {
            mobileMenu.classList.toggle('open');
        });
    }

    // Close mobile menu on outside click
    document.addEventListener('click', function (e) {
        if (mobileMenu && mobileMenu.classList.contains('open')) {
            if (!mobileMenu.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
                mobileMenu.classList.remove('open');
            }
        }
    });

    // Fix all broken images with local placeholder
    document.querySelectorAll('img').forEach(function (img) {
        if (!img.complete || img.naturalWidth === 0) {
            img.onerror = function () {
                if (this.src !== window.location.origin + PLACEHOLDER) {
                    this.src = PLACEHOLDER;
                }
                this.onerror = null;
            };
        }
        img.addEventListener('error', function () {
            if (this.src !== window.location.origin + PLACEHOLDER) {
                this.src = PLACEHOLDER;
            }
            this.onerror = null;
        });
    });

    // Size selection validation
    const addToCartForm = document.querySelector('.add-to-cart-form');
    if (addToCartForm) {
        addToCartForm.addEventListener('submit', function (e) {
            const sizeSelected = this.querySelector('input[name="size"]:checked');
            if (!sizeSelected) {
                e.preventDefault();
                const sizeGrid = document.getElementById('sizeGrid');
                if (sizeGrid) {
                    sizeGrid.style.outline = '2px solid #e5100f';
                    sizeGrid.style.outlineOffset = '6px';
                    sizeGrid.style.borderRadius = '8px';
                    setTimeout(() => {
                        sizeGrid.style.outline = '';
                        sizeGrid.style.outlineOffset = '';
                    }, 2500);
                    sizeGrid.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            }
        });
    }

    // Smooth hover on product cards
    document.querySelectorAll('.product-card').forEach(function (card) {
        card.addEventListener('mouseenter', function () {
            this.style.willChange = 'transform';
        });
        card.addEventListener('mouseleave', function () {
            this.style.willChange = 'auto';
        });
    });

    // Color chip selection
    document.querySelectorAll('.color-chip').forEach(function (chip) {
        chip.addEventListener('click', function () {
            document.querySelectorAll('.color-chip').forEach(c => c.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // Auto-format card number
    const cardNumber = document.getElementById('cardNumber');
    if (cardNumber) {
        cardNumber.addEventListener('input', function () {
            let v = this.value.replace(/\D/g, '').substring(0, 16);
            this.value = v.replace(/(.{4})/g, '$1 ').trim();
            const icon = document.getElementById('cardIcon');
            if (icon) {
                if (v.startsWith('4')) icon.textContent = '💙';
                else if (v.startsWith('5')) icon.textContent = '🔴';
                else if (v.startsWith('3')) icon.textContent = '🟢';
                else icon.textContent = '💳';
            }
        });
    }

    const cardExpiry = document.getElementById('cardExpiry');
    if (cardExpiry) {
        cardExpiry.addEventListener('input', function () {
            let v = this.value.replace(/\D/g, '').substring(0, 4);
            if (v.length >= 2) v = v.substring(0, 2) + '/' + v.substring(2);
            this.value = v;
        });
    }

    const cardCvv = document.getElementById('cardCvv');
    if (cardCvv) {
        cardCvv.addEventListener('input', function () {
            this.value = this.value.replace(/\D/g, '').substring(0, 4);
        });
    }

    // Checkout: disable button on submit to prevent double orders
    const checkoutForm = document.getElementById('checkoutForm');
    if (checkoutForm) {
        checkoutForm.addEventListener('submit', function () {
            const btn = document.getElementById('placeOrderBtn');
            if (btn) {
                btn.textContent = 'Processing...';
                btn.disabled = true;
            }
        });
    }
});

// Qty adjust helper (for product detail)
function adjustQty(delta) {
    const input = document.getElementById('qtyInput');
    if (!input) return;
    const val = parseInt(input.value) + delta;
    if (val >= 1 && val <= 10) input.value = val;
}

// Password toggle helper
function togglePassword() {
    const input = document.getElementById('passwordInput');
    const btn = document.querySelector('.password-toggle');
    if (!input) return;
    if (input.type === 'password') {
        input.type = 'text';
        if (btn) btn.textContent = 'Hide';
    } else {
        input.type = 'password';
        if (btn) btn.textContent = 'Show';
    }
}
