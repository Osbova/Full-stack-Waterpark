<template>
  <div>
    <header id="bot">
      <div class="nav-group left-nav">
        <button class="navigation">Еда</button>
        <router-link to="/ticket" class="navigation">Билеты</router-link>
        <router-link to="/slide" class="navigation">Горки</router-link>
        <a href="https://t.me/ARESTOVAN_ZA_IZBIYENIE" target="_blank" class="navigation support-btn">Поддержка</a>
      </div>

      <h1 class="logo">
        <span class="let1">А</span>
        <span class="let2">к</span>
        <span class="let3">в</span>
        <span class="let4">а</span>
        <span class="let5">в</span>
        <span class="let6">э</span>
        <span class="let7">й</span>
      </h1>

      <div class="nav-group right-nav">
        <div class="wallet-badge">
          <span class="wallet-icon">💳</span>
          <span class="wallet-balance">0 ₽</span>
        </div>
        <button class="navigation profile-btn">Пополнить</button>
      </div>
    </header>


    <main class="slides-container">
      <h2 class="section-title">Наши Горки</h2>

      <div class="slides-list">
        <article 
          v-for="(slide, index) in slides" 
          :key="slide.id" 
          class="slide-card"
          :class="{ 'reverse': index % 2 !== 0 }"
        >

          <div class="slide-image-wrapper">
            <img :src="slide.image" :alt="slide.title" class="slide-image" />
            <span class="badge" :class="slide.tagClass">{{ slide.tag }}</span>
          </div>

        
          <div class="slide-content">
            <h3 class="slide-title">{{ slide.title }}</h3>
            <p class="slide-description">{{ slide.description }}</p>
            
            <div class="slide-stats">
              <div class="stat-item">
                <span class="stat-label">Высота</span>
                <span class="stat-value">{{ slide.height }}</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Скорость</span>
                <span class="stat-value">{{ slide.speed }}</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Возраст</span>
                <span class="stat-value">{{ slide.age }}</span>
              </div>
            </div>
          </div>
        </article>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'

import slide1Img from '../assets/Slides/slide1.png'
import slide2Img from '../assets/Slides/slide2.png'
import slide3Img from '../assets/Slides/slide3.png'
import slide4Img from '../assets/Slides/slide4.png'

const slides = ref([
  {
    id: 1,
    title: 'Гонка',
    description: 'Многополосная открытая горка для любителей скорости и соревнований. Несколько дорожек позволяют одновременно спускаться нескольким посетителям и устроить настоящую гонку. Спуск проходит по прямой трассе с плавным ускорением и ярким финишем.',
    height: '18 м',
    speed: 'до 40 км/ч',
    age: '10+',
    image: slide1Img
  },
  {
    id: 2,
    title: 'Шторм',
    description: 'Экстремальная водная горка с широким открытым спуском и мощными потоками воды по бокам. Перед финишем трасса резко меняет направление, создавая ощущение сильного ускорения и невесомости. Подойдёт тем, кто хочет получить максимум эмоций за короткий спуск.',
    height: '20 м',
    speed: 'до 50 км/ч',
    age: '14+',
    image: slide2Img
  },
  {
    id: 3,
    title: "Огненная воронка",
    description: "Захватывающий спуск по закрытому скоростному тоннелю, который на высокой скорости выносит вас в гигантскую открытую чашу. Вы сделаете несколько стремительных кругов по центробежной спирали, преодолевая силу гравитации, после чего с брызгами вылетите в финишный бассейн. Идеально для тех, кто ищет настоящий драйв и яркие эмоции.",
    height: "35 м",
    speed: "до 70 км/ч",
    age: "15+",
    image: slide3Img

  },
  {
    id: 4,
    title: "Центрифуга",
    description: 'Стремительный спуск по крутым виражам закрытого тоннеля превращается в невероятное приключение, когда вы на высокой скорости врываетесь в огромную чашу-воронку. Кружась по спирали и преодолевая гравитацию, вы промчитесь по самой грани эмоций до финального освежающего всплеска. Готовы к самому захватывающему спуску?',
    height: "40 м",
    speed: "до 75 км/ч",
    age: "12+",
    image: slide4Img
  }

])
</script>

<style scoped>
:global(body) {
  margin: 0;
  padding: 0;
}

#bot {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(226, 232, 240, 0.8);
  padding: 12px 40px;
  background-color: #ffffff;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
}

.nav-group {
  display: flex;
  align-items: center;
  gap: 12px;
  flex: 1;
}

.support-btn {
  text-decoration: none; 
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.right-nav {
  justify-content: flex-end;
}

.navigation {
  background: transparent;
  border: none;
  cursor: pointer;
  color: #334155;
  font-weight: 700;
  font-size: 1.05rem;
  padding: 8px 16px;
  border-radius: 10px;
  transition: all 0.2s ease;
  text-decoration: none; 
}

.navigation:hover {
  color: #0077b6;
  background-color: #f1f5f9;
}

.wallet-badge {
  display: flex;
  align-items: center;
  gap: 6px;
  background-color: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 6px 14px;
  border-radius: 20px;
  font-weight: 700;
  color: #0f172a;
  font-size: 0.95rem;
}

.wallet-icon {
  font-size: 1.1rem;
}

.profile-btn {
  background-color: #0077b6;
  color: #ffffff;
}

.profile-btn:hover {
  background-color: #00b4d8;
  color: #ffffff;
}

.logo {
  font-size: 3.2rem;
  font-weight: 900;
  margin: 0 20px;
  letter-spacing: 6px;
  text-align: center;
  white-space: nowrap;
  line-height: 1;
}

.let1 { color: #00b4d8; } 
.let2 { color: #0077b6; } 
.let3 { color: #48cae4; } 
.let4 { color: #52b788; } 
.let5 { color: #ffb703; } 
.let6 { color: #fb8500; }
.let7 { color: #e63946; }


.slides-container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 40px 20px;
}

.section-title {
  text-align: center;
  font-size: 2.2rem;
  color: #0f172a;
  margin-bottom: 40px;
  font-weight: 800;
}

.slides-list {
  display: flex;
  flex-direction: column;
  gap: 50px;
}

.slide-card {
  display: flex;
  align-items: center;
  gap: 40px;
  background: #ffffff;
  border-radius: 24px;
  padding: 24px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  border: 1px solid #f1f5f9;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.slide-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
}

.slide-card.reverse {
  flex-direction: row-reverse;
}

.slide-image-wrapper {
  flex: 1;
  position: relative;
  height: 300px;
  border-radius: 18px;
  overflow: hidden;
}

.slide-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.slide-card:hover .slide-image {
  transform: scale(1.03);
}

.badge {
  position: absolute;
  top: 16px;
  left: 16px;
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 700;
  color: #fff;
}

.danger { background-color: #e63946; }
.warning { background-color: #fb8500; }

.slide-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.slide-title {
  font-size: 1.8rem;
  color: #0077b6;
  margin: 0;
}

.slide-description {
  color: #475569;
  line-height: 1.6;
  font-size: 1rem;
  margin: 0;
}

.slide-stats {
  display: flex;
  gap: 20px;
  background-color: #f8fafc;
  padding: 12px 20px;
  border-radius: 14px;
  border: 1px solid #e2e8f0;
}

.stat-item {
  display: flex;
  flex-direction: column;
}

.stat-label {
  font-size: 0.75rem;
  color: #64748b;
  text-transform: uppercase;
  font-weight: 600;
}

.stat-value {
  font-size: 1rem;
  font-weight: 700;
  color: #0f172a;
}

.action-btn {
  align-self: flex-start;
  background-color: #0077b6;
  color: white;
  border: none;
  padding: 10px 24px;
  border-radius: 12px;
  font-weight: 700;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.action-btn:hover {
  background-color: #00b4d8;
}

@media (max-width: 768px) {
  #bot {
    flex-direction: column;
    padding: 15px 10px;
    gap: 15px;
  }

  .logo {
    font-size: 2.2rem;
    letter-spacing: 3px;
    margin: 5px 0;
    order: -1;
  }

  .nav-group {
    width: 100%;
    justify-content: center;
    flex-wrap: wrap;
    gap: 8px;
  }

  .navigation {
    padding: 6px 12px;
    font-size: 0.9rem;
  }

  .slide-card,
  .slide-card.reverse {
    flex-direction: column;
    padding: 16px;
  }

  .slide-image-wrapper {
    width: 100%;
    height: 220px;
  }

  .action-btn {
    width: 100%;
  }
}
</style>