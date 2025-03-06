<script setup >
import { ref } from 'vue'
import axios from 'axios'

let ways = ref([
  { ischoose: 0, name: "Caesar cipher" },
  { ischoose: 0, name: "Vigenere Cipher" }
])
let encry = ref("")
let decry = ref("")
const key = ref("")


function selectway(clickedIndex) {
  ways.value = ways.value.map((item, index) => ({
    ...item,
    ischoose: index === clickedIndex ? 1 : 0
  }))
}

async function encrypt() {
  const response = await axios.post(
    "http://127.0.0.1:8000/api/encrypt", 
    {
    text: encry.value,
    algorithm: getSelectedAlgorithm(),
    key: key.value
  })
  decry.value = response.data.result
}

async function decrypt() {
  const response = await axios.post(
    'http://127.0.0.1:8000/api/decrypt', 
    {
    text: decry.value,
    algorithm: getSelectedAlgorithm(),
    key: key.value
  })
  encry.value = response.data.result
}

function getSelectedAlgorithm() {
  const selected = ways.value.find(item => item.ischoose === 1)
  return selected ? selected.name : null
}

</script>

<template>
  <div class="header">
    <h1>Online En/Decryption</h1>
    <div class="accent-line"></div>
  </div>

  <div class="container">
    <div class="algorithm-selector">
      <div 
        v-for="(i, index) in ways" 
        class="algorithm-card" 
        :class="{ 'selected': i.ischoose }" 
        @click="selectway(index)"
      >
        <div class="card-content">
          <div class="card-icon">🔒</div>
          <div class="card-name">{{ i.name }}</div>
        </div>
      </div>
    </div>

    <div class="crypto-container">
      <div class="input-section">
        <textarea 
          class="crypto-input" 
          placeholder="Enter plain text..."
          v-model="encry"
        ></textarea>
      </div>

      <div class="control-panel">
        <div class="key-input">
          <input 
            type="text" 
            placeholder="Encryption Key"
            v-model="key"
          >
          <div class="tooltip">?</div>
        </div>
        <div class="action-buttons">
          <button class="encrypt-btn" @click="encrypt">
            <span>Encrypt →</span>
          </button>
          <button class="decrypt-btn" @click="decrypt">
            <span>← Decrypt</span>
          </button>
        </div>
      </div>

      <div class="input-section">
        <textarea 
          class="crypto-input" 
          placeholder="Enter cipher text..."
          v-model="decry"
        ></textarea>
      </div>
    </div>
  </div>
</template>

<style scoped>
.header {
  text-align: center;
  padding: 2rem 0;
  background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
  color: white;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.header h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.accent-line {
  width: 80px;
  height: 4px;
  background: #fff;
  margin: 0 auto;
  border-radius: 2px;
}

.container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.algorithm-selector {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
  margin-bottom: 3rem;
}

.algorithm-card {
  flex: 0 1 280px;
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border: 2px solid transparent;
}

.algorithm-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.algorithm-card.selected {
  border-color: #6366f1;
  background: #f8fafc;
}

.card-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.card-icon {
  font-size: 2rem;
}

.card-name {
  font-size: 1.1rem;
  font-weight: 500;
  color: #1e293b;
}

.crypto-container {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: 2rem;
  align-items: center;
}

.input-section {
  height: 300px;
}

.crypto-input {
  width: 100%;
  height: 100%;
  padding: 1.5rem;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  resize: none;
  font-family: 'Courier New', monospace;
  font-size: 1.1rem;
  transition: all 0.3s ease;
}

.crypto-input:focus {
  outline: none;
  border-color: #6366f1;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
}

.control-panel {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  min-width: 260px;
}

.key-input {
  position: relative;
}

.key-input input {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 2px solid #e2e8f0;
  border-radius: 6px;
  font-size: 1rem;
}

.tooltip {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  width: 20px;
  height: 20px;
  background: #e2e8f0;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  cursor: help;
}

.action-buttons {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

button {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.encrypt-btn {
  background: #10b981;
  color: white;
}

.encrypt-btn:hover {
  background: #059669;
  transform: translateX(4px);
}

.decrypt-btn {
  background: #3b82f6;
  color: white;
}

.decrypt-btn:hover {
  background: #2563eb;
  transform: translateX(-4px);
}

@media (max-width: 768px) {
  .crypto-container {
    grid-template-columns: 1fr;
  }
  
  .control-panel {
    order: 1;
    min-width: auto;
  }
}
</style>
