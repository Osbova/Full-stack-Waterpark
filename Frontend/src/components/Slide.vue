<template>
  <div>
    <header id="bot">
      <div class="nav-group left-nav">
        <button class="navigation">Еда</button>
        <button class="navigation">Билеты</button>
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
        <button class="navigation profile-btn">Профиль</button>
      </div>
    </header>
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