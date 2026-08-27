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

    <main class="main-content">
      <section class="hero-section">
        <img src="../assets/Logo_menu.png" alt="Аквапарк" class="hero-bg" />
        <div class="hero-overlay"></div>

        <div class="hero-content">
          <h2 class="hero-title">Незабываемый отдых и эмоции</h2>
          <p class="hero-subtitle">Окунитесь в мир водных развлечений прямо сейчас</p>
          <router-link to="/ticket" class="buy-ticket-btn">Купить билет</router-link> 
        </div>
      </section>
    </main>
  </div>
</template>

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

.main-content {
  padding: 0;
  width: 100%;
}

.hero-section {
  position: relative;
  width: 100%;
  height: calc(100vh - 75px); 
  border-radius: 0;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: none;
}

.hero-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 1;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle, rgba(0, 0, 0, 0.3) 0%, rgba(0, 0, 0, 0.7) 100%);
  z-index: 2;
}

.hero-content {
  position: relative;
  z-index: 3;
  text-align: center;
  color: #ffffff;
  max-width: 650px;
  padding: 0 20px;
}

.hero-title {
  font-size: 3rem;
  font-weight: 900;
  margin-bottom: 12px;
  text-shadow: 0 4px 12px rgba(0, 0, 0, 0.6);
}

.hero-subtitle {
  font-size: 1.25rem;
  color: #e2e8f0;
  margin-bottom: 32px;
  font-weight: 500;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.6);
}

.buy-ticket-btn {
  background: linear-gradient(135deg, #00b4d8 0%, #0077b6 100%);
  color: #ffffff;
  font-size: 1.25rem;
  font-weight: 800;
  padding: 18px 48px;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  box-shadow: 0 8px 25px rgba(0, 180, 216, 0.4);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  font-family: inherit;
  text-decoration: none;
}

.buy-ticket-btn:hover {
  transform: translateY(-3px) scale(1.02);
  box-shadow: 0 12px 30px rgba(0, 180, 216, 0.6);
  background: linear-gradient(135deg, #48cae4 0%, #0077b6 100%);
}

.buy-ticket-btn:active {
  transform: translateY(-1px) scale(0.98);
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

  .hero-title {
    font-size: 1.8rem;
  }

  .hero-subtitle {
    font-size: 1rem;
    margin-bottom: 20px;
  }

  .buy-ticket-btn {
    padding: 12px 30px;
    font-size: 1rem;
  }
}
</style>