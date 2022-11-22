sequenceDiagram
    Jostain->>Kone: Machine()
    Kone->>Tankki: FuelTank()
    Kone->>Tankki: fill(40)
    Kone->>Moottori: Engine(Tankki)
    Jostain->>Kone: drive()
    Kone->>Moottori: start()
    Moottori->>Tankki: consume(5)
    Kone->>Moottori: is_running()
    Moottori-->>Kone: True
    Kone->>Moottori: use_energy()
    Moottori->>Tankki: consume(10)