# 🎨 DavaWasab Styleset

> UI Components Library for Future Development & Interface Design

## 📋 Overview

This styleset contains a complete collection of UI components, styles, colors, animations, and effects used in the DavaWasab Portfolio. It serves as a reference and foundation for future interface development.

## 📁 Files

- **`styleset.html`** - Interactive showcase of all UI components
- **`styleset.css`** - Complete stylesheet with all design tokens and components
- **`styleset.js`** - JavaScript utilities and interactive features

## 🎨 Color Palette

### Primary Colors
- **Accent Green**: `#E0FF00` - Main accent color
- **Secondary Green**: `#87C93D` - Secondary accent
- **Dark Background**: `#01000D` - Main background
- **Light Text**: `#F0FFD0` - Primary text color

### Usage
```css
:root {
    --accent-green: #E0FF00;
    --secondary-green: #87C93D;
    --dark-bg: #01000D;
    --text-white: #F0FFD0;
}
```

## 📝 Typography

### Fonts
- **Unbounded** - Display font (headings, titles)
- **Montserrat** - Body font (text, UI elements)

### Hierarchy
```css
/* Hero Title */
font-family: 'Unbounded', sans-serif;
font-size: 48px;
font-weight: 900;

/* Section Title */
font-family: 'Montserrat', sans-serif;
font-size: 32px;
font-weight: 700;

/* Widget Title */
font-family: 'Montserrat', sans-serif;
font-size: 18px;
font-weight: 700;

/* Body Text */
font-family: 'Montserrat', sans-serif;
font-size: 15px;
font-weight: 400;
```

## 🔘 Buttons

### Primary Button
```html
<button class="btn btn-primary">Primary Button</button>
```

### Secondary Button
```html
<button class="btn btn-secondary">Secondary Button</button>
```

### Large Buttons
```html
<button class="btn btn-primary btn-large">Large Primary</button>
```

## 📦 Widgets

### Widget Sizes
- **Small**: `widget-small` - Compact information blocks
- **Medium**: `widget-medium` - Standard content
- **Large**: `widget-large` - Extended content (spans 2 columns)

### Widget Structure
```html
<div class="widget widget-medium">
    <div class="widget-header">
        <span class="widget-icon">
            <svg>...</svg>
        </span>
        <h3>Widget Title</h3>
    </div>
    <div class="widget-content">
        <p>Widget content...</p>
    </div>
</div>
```

## 🏷️ Tags

### Language Tags
```html
<div class="language-tags">
    <span class="tag">UA</span>
    <span class="tag">EN</span>
    <span class="tag">RU</span>
</div>
```

### Currency Tags
```html
<div class="payment-currencies">
    <span class="currency-tag">UAH</span>
    <span class="currency-tag">USD</span>
    <span class="currency-tag">EUR</span>
</div>
```

## 🎯 Icons

All icons use Material Design style with:
- Size: `22px × 22px`
- Stroke width: `2px`
- Color: `var(--accent-green)`

### Icon Container
```html
<div class="widget-icon">
    <svg viewBox="0 0 24 24">
        <path d="..."/>
    </svg>
</div>
```

## ✨ Effects & Animations

### Hover Lift
```css
.hover-lift {
    transition: all 0.3s ease;
}

.hover-lift:hover {
    transform: translateY(-8px);
    box-shadow: var(--shadow-hover);
}
```

### Fade In
```css
.fade-in {
    animation: fadeInUp 1s ease-out;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
```

### Glow Effect
```css
.glow-effect:hover {
    border-color: var(--accent-green);
    box-shadow: 0 0 30px rgba(224, 255, 0, 0.3);
}
```

## 🌌 Backgrounds

### Dark Background
```css
background: rgba(1, 0, 13, 0.95);
```

### Card Background
```css
background: rgba(255, 255, 255, 0.03);
backdrop-filter: blur(10px);
```

### Gradient Background
```css
background: linear-gradient(135deg, 
    rgba(224, 255, 0, 0.1), 
    rgba(135, 201, 61, 0.05)
);
```

## ✨ Particles System

Animated background particles for visual depth:

```javascript
createParticles(); // Creates 50 floating particles
```

### Particle Properties
- Count: 50
- Size: 2-5px
- Duration: 20-45s
- Opacity: 0.3 (constant)
- Movement: Random translation

## 🎭 Shadows

```css
/* Default Shadow */
--shadow-default: 0 8px 32px rgba(0, 0, 0, 0.3);

/* Hover Shadow */
--shadow-hover: 0 12px 48px rgba(224, 255, 0, 0.15);
```

## 🔲 Borders

```css
/* Default Border */
--border-default: 1px solid rgba(224, 255, 0, 0.15);

/* Hover Border */
--border-hover: 1px solid rgba(224, 255, 0, 0.3);
```

## 📱 Responsive Design

### Breakpoints
- Mobile: `max-width: 768px`
- Tablet: `768px - 1024px`
- Desktop: `1024px+`

### Grid System
```css
.widget-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 24px;
}
```

## 🚀 Usage

### 1. Open Styleset
```bash
# Open styleset.html in browser
open docs/styleset.html
```

### 2. Copy Components
Browse the styleset and copy the HTML/CSS/JS code for any component you need.

### 3. Customize
Modify colors, sizes, and styles using CSS variables.

## 🛠️ JavaScript Utilities

### Available Functions
```javascript
// Create particles background
DavaWasabStyleset.createParticles();

// Copy text to clipboard
DavaWasabStyleset.copyToClipboard('text');

// Initialize smooth scroll
DavaWasabStyleset.initSmoothScroll();

// Initialize code copy
DavaWasabStyleset.initCopyCode();

// Initialize widget interactions
DavaWasabStyleset.initWidgetInteractions();
```

## 📝 Notes

- All components are production-ready
- Fully responsive and mobile-friendly
- Optimized for performance
- Accessible and semantic HTML
- Modern CSS with custom properties
- Smooth animations and transitions

## 🎯 Best Practices

1. **Use CSS Variables** - Always use defined color variables
2. **Maintain Consistency** - Follow the established design patterns
3. **Optimize Performance** - Use `backdrop-filter` sparingly
4. **Test Responsiveness** - Check all breakpoints
5. **Accessibility** - Ensure proper contrast and semantic HTML

## 📄 License

For development use only. Part of DavaWasab Portfolio project.

---

**Created by**: Dava_Wasab  
**Version**: 1.0.0  
**Last Updated**: November 2024
