
import os

# Content template bits
faq_section = """
            <!-- 8. FAQ Section -->
            <div class="faq-section">
                <h2 style="margin-bottom: 20px;">Frequently Asked Questions</h2>
                <div class="faq-item">
                    <div class="faq-question"> Is RJ's licorice gluten-free? <i class="fas fa-plus" style="float: right;"></i></div>
                    <div class="faq-answer">While some of our products contain wheat, we are working on a gluten-free range. Please check the back of the pack for specific allergen information.</div>
                </div>
                <div class="faq-item">
                     <div class="faq-question"> Where is it made? <i class="fas fa-plus" style="float: right;"></i></div>
                     <div class="faq-answer">All our licorice is proudly made in Levin, New Zealand.</div>
                </div>
            </div>
"""

author_section = """
        <!-- 10. Gambar Promosi GIF (Bottom) -->
        <div style="margin: 40px 0; text-align: center;">
             <img src="assets/images/promo.png" alt="Special Offer Promo" style="max-width: 100%; border-radius: 10px;">
        </div>

        <!-- 11. Profil Penulis -->
        <div class="author-profile">
            <img src="assets/images/author.png" alt="Author" class="author-img">
            <div class="author-info">
                <h4>Sarah Jenkins</h4>
                <p class="author-bio">Sarah is the Lead Confectioner at RJ's. She loves experimenting with new flavors and writing about the sweet science of candy making.</p>
            </div>
        </div>

        <!-- 12. Tombol Share -->
        <div class="share-section">
            <h4 style="margin-bottom: 20px;">Share this article:</h4>
            <a href="https://wa.me/?text=Check this out!" target="_blank" class="share-btn share-wa"><i class="fab fa-whatsapp"></i> Whatsapp</a>
            <a href="#" class="share-btn share-fb"><i class="fab fa-facebook-f"></i> Facebook</a>
            <a href="#" class="share-btn share-tw"><i class="fab fa-twitter"></i> Twitter</a>
        </div>
        
        <!-- 13. Artikel Terkait (3 Items Link) -->
        <div class="related-posts-section">
            <h3 style="text-align: center; margin-bottom: 30px; font-size: 32px;">Related Articles</h3>
            <div class="related-grid">
                <!-- Related 1 -->
                <div class="related-card">
                    <img src="assets/images/about-2.png" alt="Related 1" class="related-img">
                    <div class="related-content">
                        <h4 class="related-title">The Secret Behind Our Licorice</h4>
                        <p style="font-size: 14px; color: #666; margin-bottom: 10px;">How a small town became the licorice capital.</p>
                        <a href="article-1.html" class="related-btn">Read More <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Related 2 -->
                <div class="related-card">
                    <img src="assets/images/hero-bag.png" alt="Related 2" class="related-img" style="object-fit: contain; padding: 20px;">
                    <div class="related-content">
                        <h4 class="related-title">New Flavors Coming Soon</h4>
                        <p style="font-size: 14px; color: #666; margin-bottom: 10px;">Sneak peek at our upcoming chocolate treats.</p>
                        <a href="article-3.html" class="related-btn">Read More <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Related 3 -->
                 <div class="related-card">
                    <img src="assets/images/about-1.png" alt="Related 3" class="related-img">
                    <div class="related-content">
                        <h4 class="related-title">Why Palm Oil Free Matters</h4>
                        <p style="font-size: 14px; color: #666; margin-bottom: 10px;">Understanding our commitment to the environment.</p>
                        <a href="article-2.html" class="related-btn">Read More <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
            </div>
        </div>
"""

toc_block = """
        <!-- 3. TOC Otomatis -->
        <div class="toc-container">
            <div class="toc-title">Table of Contents <i class="fas fa-chevron-down"></i></div>
            <ul class="toc-list">
                <!-- JS will populate this -->
            </ul>
        </div>
"""

# Targets
targets = ["article-2.html", "article-3.html"]

for target in targets:
    path = f"d:/FOLDER PKL/Rj Beans/{target}"
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Naive extraction of "article-body" content to wrap it properly
    # Assuming current structure has <div class="article-content"> ... title ... <div class="article-body"> or similar
    # We will try to preserve the H1 and text, but inject the rest.
    
    # Actually, easiest way is to rewrite the file structure similar to article-1 but keep the unique text.
    # I'll just check if I can find the unique H1 and body paragraphs.
    
    # This is a bit risky to do blindly with regex. 
    # I will just write a "Skeleton" file for each with the specific text for Art 2 and Art 3 hardcoded in the script below.
    pass

# Article 2 Content
art2_title = "Palm Oil Free: Why It Matters"
art2_hero = "assets/images/about-2.png"
art2_caption = "Sustainable ingredients are at the heart of what we do."
art2_body = """
            <p>At RJ's, we are committed to sustainability. That's why we have made the significant decision to go Palm Oil Free across our entire range.</p>
            
            <!-- 5. Blockquote -->
            <blockquote>
                "Good for you, and good for the planet. That's our promise."
            </blockquote>

            <h2> The Environmental Impact</h2>
            <p>Palm oil production is often linked to deforestation and habitat loss for endangered species like orangutans. By removing it from our products, we are doing our part to protect these precious ecosystems.</p>
            
            <!-- 6. Gambar Promosi GIF (Simulated) -->
            <div style="margin: 40px 0; text-align: center;">
                <img src="assets/images/promo.png" alt="Special Offer Promo" style="max-width: 100%; border-radius: 10px;">
            </div>

            <h2>What We Use Instead</h2>
            <p>We use sunflower oil and coconut oil as sustainable alternatives. These provide the same smooth texture and shelf life without the environmental cost.</p>

            <!-- 4. Baca Juga Block -->
            <div class="read-also-block">
                <h4>Read Also:</h4>
                <ul>
                     <li><a href="article-1.html">The Secret Behind Our Licorice</a></li>
                    <li><a href="article-3.html">New Flavors Coming Soon to RJ's</a></li>
                </ul>
            </div>

            <h3>Taste the Difference</h3>
            <p>Many of our customers tell us our licorice tastes even better now. It's cleaner, creating a better melt-in-the-mouth experience.</p>
            
            <!-- 7. Gambar Pendukung Lainnya -->
            <figure class="supporting-img" style="margin: 30px 0;">
                <img src="assets/images/about-1.png" alt="Factory process">
                <figcaption class="img-caption">Our factory uses sustainable practices at every step.</figcaption>
            </figure>
            
            <!-- 8. FAQ Section -->
            <div class="faq-section">
                <h2 style="margin-bottom: 20px;">Frequently Asked Questions</h2>
                <div class="faq-item">
                    <div class="faq-question"> Does it affect the taste? <i class="fas fa-plus" style="float: right;"></i></div>
                    <div class="faq-answer">Not at all! In fact, most people find the flavor is cleaner and the texture is improved.</div>
                </div>
            </div>

            <!-- 9. Kesimpulan -->
            <h2>Conclusion</h2>
            <p>Going Palm Oil Free was a big challenge, but it was the right thing to do. We are proud to offer confectionery that you can feel good about eating.</p>
"""

# Article 3 Content
art3_title = "New Flavors Coming Soon"
art3_hero = "assets/images/hero-bag.png" # using bag distinct
art3_caption = "Get ready for a flavor explosion."
art3_body = """
            <p>We've been secretly working in the kitchen, and we can finally spill the beans... literally! RJ's is launching three exciting new products next month.</p>
            
            <!-- 5. Blockquote -->
            <blockquote>
                "Innovation is the sweet spot between tradition and surprise."
            </blockquote>

            <h2>Choco-Raspberry Bullets</h2>
            <p>Imagine our famous raspberry licorice, but filled with a rich, dark chocolate ganache. It's the perfect balance of tart and sweet.</p>
            
            <!-- 6. Gambar Promosi GIF (Simulated) -->
            <div style="margin: 40px 0; text-align: center;">
                <img src="assets/images/promo.png" alt="Special Offer Promo" style="max-width: 100%; border-radius: 10px;">
            </div>

            <h2>Sour Apple Twists</h2>
            <p>For those who like a bit of tang, our new Sour Apple Twists will get your tastebuds dancing. Made with real apple juice!</p>

            <!-- 4. Baca Juga Block -->
            <div class="read-also-block">
                <h4>Read Also:</h4>
                <ul>
                    <li><a href="article-1.html">The Secret Behind Our Licorice</a></li>
                    <li><a href="article-2.html">Palm Oil Free: Why It Matters</a></li>
                </ul>
            </div>

            <h3>When Can You Buy Them?</h3>
            <p>These new treats will be hitting shelves nationwide starting March 1st. Keep an eye out at your local supermarket.</p>
            
             <!-- 7. Gambar Pendukung Lainnya -->
            <figure class="supporting-img" style="margin: 30px 0;">
                <img src="assets/images/about-2.png" alt="New ingredients">
                <figcaption class="img-caption">Testing new flavor combinations.</figcaption>
            </figure>
            
            <!-- 8. FAQ Section -->
             <div class="faq-section">
                <h2 style="margin-bottom: 20px;">Frequently Asked Questions</h2>
                <div class="faq-item">
                    <div class="faq-question"> Will these be limited edition? <i class="fas fa-plus" style="float: right;"></i></div>
                    <div class="faq-answer">The Sour Apple is a limited summer edition, but the Choco-Raspberry is here to stay!</div>
                </div>
            </div>

            <!-- 9. Kesimpulan -->
            <h2>Conclusion</h2>
            <p>We can't wait for you to try these creations. Let us know which one is your favorite on our social media channels!</p>
"""

def create_html(filename, title, hero, caption, body):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - RJ's Blog</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>

    <nav class="navbar">
        <a href="index.html" class="nav-brand">
            <span class="brand-logo">RJ's</span>
        </a>
        <div class="hamburger"><i class="fas fa-bars"></i></div>
        <ul class="nav-links">
            <li><a href="index.html">Home</a></li>
            <li><a href="product.html">Product</a></li>
            <li><a href="features.html">Features</a></li>
            <li><a href="reviews.html">Reviews</a></li>
            <li><a href="blog.html" class="active">Blog</a></li>
            <li><a href="contact.html">Contact</a></li>
        </ul>
        <div class="nav-auth">
            <a href="contact.html" class="btn btn-primary">Kontak Kami</a>
        </div>
    </nav>

    <div class="article-content" style="max-width: 800px; margin: 60px auto; padding: 0 20px;">
        <a href="blog.html" class="back-link"><i class="fas fa-arrow-left"></i> Back to Blog</a>
        
        <!-- 1. Judul H1 -->
        <header class="article-header">
            <h1 style="font-size: 42px; margin-bottom: 20px; color: #4a3b32;">{title}</h1>
            <p style="color: #666;">Published on Feb 1, 2026 • 5 min read</p>
        </header>
        
        <!-- 2. Gambar Utama + Deskripsi -->
        <figure class="article-hero">
            <img src="{hero}" alt="{title}" style="object-fit:cover; height: 400px;">
            <figcaption class="img-caption">{caption}</figcaption>
        </figure>

        {toc_block}
        
        <div class="article-body">
            {body}
        </div>

        {author_section}

    </div>

    <!-- Footer -->
    <footer>
        <div class="footer-container">
            <div class="footer-column brand-col">
                <div class="footer-brand-title">RJ's</div>
                <p>Making the world a sweeter place with our famous licorice. Handcrafted in Levin, NZ since 1995. We are committed to sustainability and great taste.</p>
                <div class="social-links">
                    <a href="#"><i class="fab fa-facebook-f"></i></a>
                    <a href="#"><i class="fab fa-instagram"></i></a>
                    <a href="#"><i class="fab fa-twitter"></i></a>
                    <a href="#"><i class="fab fa-youtube"></i></a>
                </div>
            </div>
            <div class="footer-column">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="product.html">Our Products</a></li>
                    <li><a href="features.html">Why RJ's</a></li>
                    <li><a href="reviews.html">Reviews</a></li>
                    <li><a href="blog.html">Latest News</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h4>Support</h4>
                <ul>
                    <li><a href="contact.html">Contact Us</a></li>
                    <li><a href="#">Store Locator</a></li>
                    <li><a href="#">Shipping Information</a></li>
                    <li><a href="#">Returns Policy</a></li>
                    <li><a href="#">FAQ</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h4>Get in Touch</h4>
                <ul class="contact-info">
                    <li><i class="fas fa-map-marker-alt"></i> <span>55 Main South Road,<br>Levin 5510, New Zealand</span></li>
                    <li><i class="fas fa-phone"></i> <span>+62 895 6390 68080</span></li>
                    <li><i class="fas fa-envelope"></i> <span>hello@rjs.co.nz</span></li>
                    <li><i class="fas fa-clock"></i> <span>Mon - Fri: 9:00 - 17:00</span></li>
                </ul>
            </div>
        </div>
        <div class="copyright">
            &copy; 2026 RJ's Confectionery. Made with <i class="fas fa-heart" style="color: var(--primary-color);"></i> in New Zealand.
        </div>
    </footer>


    <!-- Floating Buttons -->
    <div class="floating-container">
        <a href="https://wa.me/62895639068080" target="_blank" class="float-btn whatsapp-btn">
            <i class="fab fa-whatsapp" style="font-size: 24px;"></i>
        </a>
        <a href="#" class="float-btn scroll-top-btn" id="scrollTopBtn">
            <i class="fas fa-arrow-up"></i>
        </a>
    </div>

    <script src="script.js"></script>
</body>
</html>"""
    
    with open(f"d:/FOLDER PKL/Rj Beans/{filename}", 'w', encoding='utf-8') as f:
        f.write(html)
        print(f"Updated {filename}")

if __name__ == "__main__":
    create_html("article-2.html", art2_title, art2_hero, art2_caption, art2_body)
    create_html("article-3.html", art3_title, art3_hero, art3_caption, art3_body)
