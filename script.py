from engine import simulate_tx_execution

def main():
    print("Starting Gas Simulation Engine...")
    
    scenarios = [
        {"limit": 21000, "price": 25, "complexity": 1.0},
        {"limit": 150000, "price": 40, "complexity": 2.5},
        {"limit": 500000, "price": 15, "complexity": 5.0}
    ]
    
    for i, s in enumerate(scenarios, 1):
        result = simulate_tx_execution(s["limit"], s["price"], s["complexity"])
        status = "PASSED" if result["success"] else "FAILED"
        print(f"Scenario {i}: {status} | Usage: {result['actual_usage']} | Cost: {result['cost_eth']} ETH")

if __name__ == "__main__":
    main()
