# vasu-portfolio
=======# Vasu Reddy - Portfolio Website

A modern, responsive portfolio website built with HTML, CSS, and JavaScript. Features a dark theme with green accents, smooth animations, and a professional design.

## 🚀 Features

- **Modern Design**: Dark theme with green accents for a professional look
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile devices
- **Smooth Animations**: CSS animations and JavaScript interactions for enhanced UX
- **Interactive Navigation**: Sidebar navigation with smooth scrolling
- **Contact Form**: Functional contact form with validation
- **Project Showcase**: Beautiful project cards with hover effects
- **Skills Display**: Animated skill cards with percentages
- **Timeline**: Educational and experience timeline
- **Social Links**: Integrated social media links

## 📁 File Structure

```
Portfolio/
├── index.html          # Main HTML file
├── styles.css          # CSS styles and animations
├── script.js           # JavaScript functionality
├── README.md           # This file
├── resume_text.txt     # Extracted resume content
└── extract_resume.py   # Python script for PDF extraction
```

## 🛠️ Technologies Used

- **HTML5**: Semantic markup
- **CSS3**: Modern styling with Flexbox and Grid
- **JavaScript (ES6+)**: Interactive functionality
- **Font Awesome**: Icons
- **Google Fonts**: Inter font family

## 🎨 Design Features

### Color Scheme
- **Primary Background**: #0a0a0a (Dark)
- **Secondary Background**: #1a1a1a (Sidebar)
- **Accent Color**: #00ff88 (Green)
- **Text Colors**: #ffffff, #ccc, #888

### Typography
- **Font Family**: Inter (Google Fonts)
- **Weights**: 300, 400, 500, 600, 700, 800

### Animations
- Smooth page transitions
- Hover effects on cards and buttons
- Typing effect on hero title
- Scroll-triggered animations
- Parallax scrolling effects

## 📱 Responsive Breakpoints

- **Desktop**: 1200px and above
- **Tablet**: 768px - 1199px
- **Mobile**: Below 768px

## 🚀 Getting Started

1. **Clone or Download**: Get all the files in your local directory
2. **Open in Browser**: Simply open `index.html` in your web browser
3. **Customize**: Edit the content in `index.html` to match your information
4. **Deploy**: Upload to any web hosting service

## ✏️ Customization Guide

### Personal Information
Edit the following sections in `index.html`:

```html
<!-- Profile Information -->
<h1 class="name">Your Name</h1>
<div class="title">Your Title</div>

<!-- Contact Information -->
<p><i class="fas fa-envelope"></i> your.email@example.com</p>
<p><i class="fas fa-map-marker-alt"></i> Your Location</p>

<!-- Social Links -->
<a href="your-github-url" target="_blank"><i class="fab fa-github"></i></a>
<a href="your-linkedin-url" target="_blank"><i class="fab fa-linkedin"></i></a>
```

### Projects
Update the projects section with your own projects:

```html
<div class="project-card">
    <div class="project-image">
        <img src="your-project-image.jpg" alt="Project Name">
    </div>
    <div class="project-content">
        <div class="project-tags">
            <span class="tag">Technology 1</span>
            <span class="tag">Technology 2</span>
        </div>
        <h3>Project Name</h3>
        <p>Project description goes here...</p>
    </div>
</div>
```

### Skills
Modify the skills section with your expertise:

```html
<div class="skill-card">
    <div class="skill-icon">
        <i class="fab fa-python"></i>
    </div>
    <div class="skill-percentage">95%</div>
    <div class="skill-name">Python</div>
</div>
```

### Colors
To change the color scheme, edit the CSS variables in `styles.css`:

```css
:root {
    --primary-bg: #0a0a0a;
    --secondary-bg: #1a1a1a;
    --accent-color: #00ff88;
    --text-primary: #ffffff;
    --text-secondary: #ccc;
}
```

## 📧 Contact Form

The contact form includes:
- Name, Email, Phone, Subject fields
- Message textarea
- File attachment option
- Form validation
- Success message simulation

## 🔧 Advanced Customization

### Adding New Sections
1. Add a new section in the HTML
2. Add corresponding navigation item
3. Style the section in CSS
4. Add JavaScript functionality if needed

### Modifying Animations
Edit the animation properties in `script.js`:

```javascript
// Change animation timing
card.style.animationDelay = `${index * 0.1}s`;

// Modify animation duration
animation: slideInUp 0.6s ease forwards;
```

### Adding New Icons
Use Font Awesome icons by adding the appropriate class:

```html
<i class="fas fa-icon-name"></i>
<i class="fab fa-brand-name"></i>
```

## 🌐 Deployment

### GitHub Pages
1. Create a GitHub repository
2. Upload all files
3. Go to Settings > Pages
4. Select source branch
5. Your site will be available at `username.github.io/repository-name`

### Netlify
1. Drag and drop the folder to Netlify
2. Your site will be deployed instantly
3. Get a custom domain if needed

### Vercel
1. Connect your GitHub repository
2. Vercel will automatically deploy
3. Get a custom domain and SSL

## 📊 Performance Optimization

- Images are optimized and use CDN links
- CSS and JavaScript are minified
- Fonts are loaded efficiently
- Smooth scrolling and animations are hardware-accelerated

## 🔒 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Feel free to fork this project and customize it for your own portfolio. If you make improvements, consider sharing them!

## 📞 Support

If you need help customizing your portfolio, feel free to reach out or check the code comments for guidance.

---

**Built with ❤️ for showcasing your amazing work!** 
>>>>>>> f37d9eb (Initial commit of Cursor AI project)
